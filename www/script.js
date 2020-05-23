// movement of selected cell using key press
var curren_active_cell = -100
document.onkeydown = handle_key

function handle_key(event) {
    if (curren_active_cell > -100) {
        $("[data-id=" + curren_active_cell + "]").blur()
        row = ~~(curren_active_cell / 9)
        col = ~~(curren_active_cell % 9)

        e = event || window.event
        if (e.keyCode == '38') {
            row--
        } else if (e.keyCode == '40') {
            row++
        } else if (e.keyCode == '37') {
            curren_active_cell = (row) * 9 + (col - 1)
            col--
        } else if (e.keyCode == '39') {
            col++
        }
        row = row > 8 ? 8: row
        row = row < 0 ? 0: row
        col = col > 8 ? 8: col
        col = col < 0 ? 0: col
        curren_active_cell = (row) * 9 + (col)
        $("#" + curren_active_cell).click()
        // $("#" + curren_active_cell).focus()
        // cell_rules(document.getElementById(curren_active_cell))
        console.log(row +" "+ col)
    }
}

// Creating clock for the game
var quick_solve = false

function pad(d) {
    return (d < 10) ? '0' + d.toString() : d.toString();
}

var clock

function create_clock() {
    var curr_time = new Date()
    clock = setInterval(function () {
        var now = new Date()
        var diff = ~~((now - curr_time) / 1000)
        var sec = pad(~~(diff % 60))
        var min = pad(~~((diff / 60) % 60))
        var hour = pad(~~((diff / (60 * 60)) % 24))
        time = hour + ":" + min + ":" + sec
        // console.log(time)
        $('.timer').html(time)
    }, 1000)
}

// getting grid id from cell id
function get_id(i) {
    row = ~~(i / 9)
    col = i % 9

    grid_i = ~~(row / 3)
    grid_j = ~~(col / 3)
    return grid_i * 3 + grid_j
}

// Sanitizing each cell if new input is detected
function sanitize(element) {
    var e = $(element)
    if (e.val().length > 0) {
        var text = e.val()[e.val().length - 1]
        var val = text.charCodeAt(0)
        if (val < 60 && val > 48) {
            e.val(text)
            eel.validate_sudoku(e.attr("data-id"), text)
        } else {
            if (e.val().length == 1) e.val("")
            else e.val(e.val()[0])
        }
    } else {
        eel.validate_sudoku(e.attr("data-id"), "")
    }
}

// validating cell for valid entry
function cell_rules(element) {
    console.log("test")
    var e = $(element)
    curren_active_cell = parseInt(e.attr("id"))
    $(".cell").removeClass("active")
    $(".cell").removeClass("cell_rules")
    $(".grid").removeClass("cell_rules")
    $("[data-id=" + curren_active_cell + "]").focus()
    var temp = $("[data-id=" + curren_active_cell + "]").val()
    $("[data-id=" + curren_active_cell + "]").val("")
    $("[data-id=" + curren_active_cell + "]").val(temp)

    var row = ~~(parseInt(e.attr("id")) / 9)
    var col = ~~(parseInt(e.attr("id")) % 9)
    for (var i = 0; i < 9; i++) {
        $("#" + (i * 9 + col)).addClass("cell_rules")
    }
    for (var i = 0; i < 9; i++) {
        $("#" + (row * 9 + i)).addClass("cell_rules")
    }
    var grid = get_id(parseInt(e.attr("id")))
    $("#grid" + grid).addClass("cell_rules")
    $("#"+curren_active_cell).addClass("active")
}

function format_sudoku_data() {
    return data
}

$(function () {
    var i = 0
    html = ""
    for (; i < 81; i++) {
        cell = `<div class="cell" id="${i}" onclick="cell_rules(this)"></div>`
        id = get_id(i)
        html = $("#grid" + id + "").html() + cell;
        $("#grid" + id + "").html(html);
    }

    $('#new_btn').click(function () {
        var level = ["Easy", "Medium", "Hard", "Expert"]
        var i = 1
        html = ""
        $(".action_message").html("");
        for (; i < 5; i++) {
            temp = `<div class="btn btn_margin select_level" id="level${i}" data-level="${i}">${level[i - 1]}</div>`
            html = $(".action_message").html() + temp;
            $(".action_message").html(html);
        }
        close_btn = "<div class='close'>x</div>"
        html = $(".action_message").html() + close_btn;
        $(".action_message").html(html);
        $(".action_message").toggle(20);
        $('.close').on("click", function () {
            $(".action_message").toggle(20);
        });
        $('.select_level').on("click", function () {
            quick_solve = false
            eel.generate_new_sudoku($(this).attr("data-level"));
            $(".level").html(level[$(this).attr("data-level") - 1]);
            $(".cell").removeClass("empty")
            $(".cell").removeClass("solved");
            $(".cell").removeClass("error");
        });

    });
    $('#solve_btn').click(function () {
        var level = ["Quick Solve", "Visualize"]
        var i = 1
        html = ""
        $(".action_message").html("");
        for (; i < 3; i++) {
            temp = `<div class="btn btn_margin solve_mode" data-mode="${i - 1}">${level[i - 1]}</div>`
            html = $(".action_message").html() + temp;
            $(".action_message").html(html);
        }
        close_btn = "<div class='close'>x</div>"
        html = $(".action_message").html() + close_btn;
        $(".action_message").html(html);
        $(".action_message").toggle(20);
        $('.close').on("click", function () {
            $(".action_message").toggle(20);
        });
        $('.solve_mode').on("click", function () {
            clearInterval(clock)
            $(".cell").removeClass("cell_rules")
            $(".grid").removeClass("cell_rules")
            $(".cell").removeClass("active")
            $(".cell").removeClass("empty")
            $(".cell").removeClass("solved");
            $(".cell").removeClass("error");
            eel.solve_sudoku($(this).attr("data-mode"));
            // $(".action_message").toggle(20);
            if ($(this).attr("data-mode") == 0)
                $(".action_message").toggle(20);
            quick_solve = true
        });
    });

});


// JavaScript functions exposed to python
eel.expose(draw_sudoku)
eel.expose(update_sudoku)
eel.expose(validate)
eel.expose(done)

// Function for drawing sudoku
function draw_sudoku(data) {
    clearInterval(clock)
    $('.timer').html("00:00:00")
    $(".cell").removeClass("active")
    $(".cell").removeClass("cell_rules")
    $(".grid").removeClass("cell_rules")
    for (i = 0; i < 81; i++) {
        // row and col values for corresponding i values
        row = ~~(i / 9);
        col = i % 9;

        // filling sudoku board with values
        if (data[row][col] != 0) { // cell in not empty
            if ($("#" + i).attr("empty") == "0") $("#" + i).removeClass("empty");
            $("#" + i).text(data[row][col]);
            $("#" + i).attr("empty", "0");
        } else { // cell is empty
            $("#" + i).attr("empty", "1");
            $("#" + i).addClass("empty");
            input = '<input class="input" data-id="' + i + '" oninput="sanitize(this)" ></input>'
            $("#" + i).html(input)
            // $(".input").on("change", function () {
            //     console.log("wor")
            // })
        }
    }
    // toggle level selector pane
    $(".action_message").toggle(20);
    if (!quick_solve) {
        create_clock()
        quick_solve = false
    }
}

// Function updating sudoku board during visualiztion
function update_sudoku(val, i) {
    $(".cell").removeClass("cell_rules")
    $(".grid").removeClass("cell_rules")
    if (val == 0) { // if cell value wrong during backtracking
        $("#" + i).removeClass("solved");
        $("#" + i).addClass("error");
        setTimeout(function () {
            $("#" + i).removeClass("error");
            $("#" + i).text("")
        }, 200);
    } else { // one of the valid cell value
        $("#" + i).addClass("solved");
        $("#" + i).text(val);
    }
}

// validating cell for sudoku rules while solving manually
function validate(i, bool) {
    if (bool) {
        $("[data-id="+i+"]").removeClass("error");
    } else {
        $("[data-id="+i+"]").addClass("error");
    }

}

// Game over after solving suduku
function done() {
    $(".action_message").html("");
    clearInterval(clock)
    temp = `<div class="message" data-mode="${i - 1}">Great!!<br>` + $('.timer').html() + `</div>`
    html = $(".action_message").html() + temp;
    $(".action_message").html(html);
    close_btn = "<div class='close'>x</div>"
    html = $(".action_message").html() + close_btn;
    $(".action_message").html(html);
    $(".action_message").toggle(20);
    $('.close').on("click", function () {
        $(".action_message").toggle(20);
    });
}