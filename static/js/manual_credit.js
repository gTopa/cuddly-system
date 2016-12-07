$('#add_user').on('click', function (e) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
	if (xhttp.readyState == 4 && xhttp.status == 200) {
	    var table = document.getElementById("users");
	    var row = table.insertRow(1);
	    var cell1 = row.insertCell(0);
	    var cell2 = row.insertCell(1);
	    cell1.innerHTML = xhttp.responseText.split(';')[0]
	    cell2.innerHTML = xhttp.responseText.split(';')[1]
	    document.getElementById('list_of_ids').value = document.getElementById('list_of_ids').value + "," + xhttp.responseText.split(';')[1]
	}
	else if (xhttp.readyState == 4 && xhttp.status == 404) {
	    window.alert('There is no tutor with that id')
	}
    }
    var tested_users = document.getElementById('list_of_ids').value.split(',');
    var found = false;
    for (var i = 0; i < tested_users.length; i++) {
	found = found || document.getElementById('four_digit').value == tested_users[i];	    
    }
    if (!found) {
	xhttp.open("GET", "../api/get_user_info/" + document.getElementById('four_digit').value);
	xhttp.send();
    }
    document.getElementById('four_digit').value = "";
});

$(document).keypress(function(e) {
    if (e.which === 13) {
	$('#add_user').click()
    }
});
