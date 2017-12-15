
    //Add Zombie
    function addZombie() {
        const name = document.getElementsByClassName('form-control')[1].value;
        const graveyard = document.getElementsByClassName('form-control')[2].value;
        const city = document.getElementsByClassName('form-control')[3].value;
        const url = encodeURI(`/AddZombie?name=${name}&graveyard=${graveyard}&city=${city}`);

        fetch(url, { method: 'POST' })
        .then(response => console.log(`Response status: ${response.status}`))

        reloadZombiesTable();
    }

    // Delete Zombie
    function deleteZombie(id, name) {
        const url = encodeURI(`/DeleteZombie?id=${id}&name=${name}`);

        fetch(url, { method: 'POST' })
        .then(response => console.log(`Response status: ${response.status}`))

        reloadZombiesTable();
        reloadHealedTable();
    }

    // Filter Zombies Table
    function filterZombies() {

        const param = document.querySelector("#filter-param").value;
        const val = document.querySelector("#filter-value").value;
        const url = encodeURI(`/FilterZombies?param=${param}&value=${val}`);

        fetch(url, { method: 'GET', mode: 'cors' })
        .then(response => response.json())
        .then(data => {

            const elementlist = document.querySelectorAll('.dynamic-zombies');
            const divArray = Array.from(elementlist);
            divArray.map((elem) => elem.remove());
            generateTable(data);
        })
    };

    // Load Zombies Table
    function loadTable() {
        const url = `/GetZombies`;

        fetch(url, { method: 'GET', mode: 'cors' })
        .then(response => response.json())
        .then(data => generateTable(data))
    };

    loadTable();

    function loadHealed() {
        const url = '/GetHealed';

        fetch(url, { method: 'GET', mode: 'cors' })
        .then(response => response.json())
        .then(data => {
            data.healed.map((item, index) => {
                const table = document.getElementById("healed");
                let row = table.insertRow(-1);
                row.className = "dynamic-healed";
                let cell1 = row.insertCell(0);
                let cell2 = row.insertCell(1);

                cell1.innerHTML = item.NAME;
                cell2.innerHTML = 'Healed';
            })
        })
    }

    loadHealed();

    // refresh zombies table
    function reloadZombiesTable() {

        const elementlist = document.querySelectorAll('.dynamic-zombies');
        const divArray = Array.from(elementlist);
        divArray.map((elem) => elem.remove());

        loadTable();
    }

    // refresh healed table
    function reloadHealedTable() {

        const elementlist = document.querySelectorAll('.dynamic-healed');
        const divArray = Array.from(elementlist);
        divArray.map((elem) => elem.remove());

        loadHealed();
    }

    function generateTable(data) {
        data.zombies.map((item, index) => {

            //create a row and a cell per item in response
            const table = document.getElementById("zombies");
            const row = table.insertRow(-1);
            const cell1 = row.insertCell(0);
            const cell2 = row.insertCell(1);
            const cell3 = row.insertCell(2);
            const cell4 = row.insertCell(3);
            const cell5 = row.insertCell(4);
            row.className = "dynamic-zombies";
            cell4.className = "text-center";
            cell5.className = "text-center";

            // add cell values
            cell1.innerHTML = item.NAME;
            cell2.innerHTML = item.GRAVEYARD;
            cell3.innerHTML = item.CITY;

            //create edit button
            const url = `/editZombie/${item.ID}`
            const btnEdit = document.createElement('a');
            const linkText = document.createTextNode("EDIT");
            btnEdit.href = url;
            btnEdit.className = "btn btn-info";
            btnEdit.appendChild(linkText);

            //create heal button
            const btnHeal = document.createElement('input');
            btnHeal.type = "button";
            btnHeal.className = "btn btn-success";
            btnHeal.value = "HEAL!";
            btnHeal.onclick = function(){ deleteZombie(item.ID, item.NAME) };

            // append buttons
            cell4.appendChild(btnEdit);
            cell5.appendChild(btnHeal);
        })
    }
