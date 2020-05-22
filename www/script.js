function get_id(i) {
    row = ~~(i / 9)
    col = i % 9

    grid_i = ~~(row / 3)
    grid_j = ~~(col / 3)
    return grid_i * 3 + grid_j
}

function sanitize(element) {
    var e = $(element)
    var text = e.val()[e.val().length - 1]
    var val = text.charCodeAt(0)
    console.log(val)
    if (val < 60 && val > 48) {
        e.val(text)
    } else {
        if (e.val().length == 1) e.val("")
        else e.val(e.val()[0])
    }
}

function format_sudoku_data() {
    return data
}

$(function () {
    var i = 0
    html = ""
    for (; i < 81; i++) {
        cell = `<div class="cell" id="${i}"></div>`
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
            eel.solve_sudoku($(this).attr("data-mode"));
            if ($(this).attr("data-mode") == 1)
                $(".action_message").toggle(20);
        });
    });

});


// JavaScript functions exposed to python
eel.expose(draw_sudoku)
eel.expose(update_sudoku)

// Function for drawing sudoku
function draw_sudoku(data) {
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
            input = '<input class="input" id="' + i + '" oninput="sanitize(this)"></input>'
            $("#" + i).html(input)
            // $(".input").on("change", function () {
            //     console.log("wor")
            // })
        }
    }
    // toggle level selector pane
    $(".action_message").toggle(20);
}

// Function updating sudoku board during visualiztion
function update_sudoku(val, i) {
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
