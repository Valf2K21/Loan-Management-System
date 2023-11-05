/*
    The Loan Management System is a web application for storing, managing, and viewing debtor, debt, and payment records.
    Copyright (C) 2023 Valfrid Galinato
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

// create a function that will handle history table generation
function table_generator(headerlist, datarows) {
    // create a row specifically for headers and store it in a variable
    let header_row = document.createElement('tr');

    // for each content of headerlist
    for (let ctr = 0; ctr < headerlist.length; ctr++) {
        // create a table header and store it in a variable
        let cell = document.createElement('th');

        // use .textContent function to fill the newly-created table header with the currently-iterated header data
        cell.textContent = headerlist[ctr];
        
        // append newly-created table header in header_row row
        header_row.appendChild(cell);
    }

    // append filled header_row in history_table table
    history_table.appendChild(header_row);

    // for each content of datarows
    for (let ctr = 0; ctr < datarows.length; ctr++) {
        // store currently iterated tuple in a variable
        let data_tuple = datarows[ctr];

        // create a table row and store it in a variable
        let data_row = document.createElement('tr');

        // for each content of data_tuple
        for (let ctr2 = 0; ctr2 < data_tuple.length; ctr2++) {
            // create a table data and store it in a variable
            let cell = document.createElement('td');

            // use .textContent function to fill the newly-created table data with the currently-iterated tuple data
            cell.textContent = data_tuple[ctr2];
            
            // append newly-created table data in data_row row
            data_row.appendChild(cell);
        }

        // append filled data_row in history_table table
        history_table.appendChild(data_row);
    }
}