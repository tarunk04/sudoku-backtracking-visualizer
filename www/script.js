function get_id(i) {
    row = ~~(i / 9)
    col = i % 9

    grid_i = ~~(row / 3)
    grid_j = ~~(col / 3)
    return grid_i * 3 + grid_j
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
        eel.generate_new_sudoku()
    });
    $('#solve_btn').click(function () {
        eel.solve_sudoku()
    });

});


eel.expose(draw_sudoku)
eel.expose(update_sudoku)

function draw_sudoku(data) {
    for (i = 0; i < 81; i++) {
        row = ~~(i / 9)
        col = i % 9
        if (data[row][col] != 0) $("#" + i).text(data[row][col])
        else $("#" + i).text("")
    }
}

function update_sudoku(val, i) {
    if (val == 0) {
        $("#" + i).removeClass("solved");
        $("#" + i).addClass("error");
        setTimeout(function () {
            $("#" + i).removeClass("error");
            $("#" + i).text("")
        }, 200);
    } else {
        $("#" + i).addClass("solved");
        $("#" + i).text(val);
    }
}