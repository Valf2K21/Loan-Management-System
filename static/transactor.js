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

// store history_table table to a variable
let history_table = document.getElementById('history_table');

// store hist_balance text input to a variable
let hist_balance = document.getElementById('hist_balance');

// create a function that any of the buttons will call once clicked
function transactor(event, transaction_type) {
    // prevent the default form submission behavior of refreshing webpage
    event.preventDefault();

    // switch-case conditional statement that do various processes depending on submitted parameter by the clicked button
    switch (transaction_type) {
        // if the button clicked is that of debtor_input
        case 'debtor_input':
            // store the submitted values in their respective variables
            let debtor_name = document.getElementById('debtor_name').value;
            let debtor_age = document.getElementById('debtor_age').value;
            let debtor_address = document.getElementById('debtor_address').value;
            let debtor_phone = document.getElementById('debtor_phone').value;

            // store the non-debtor_name variables in an array to loop through them
            let debtor_array = [debtor_age, debtor_address, debtor_phone];

            // for every value and variable index in debtor_array
            debtor_array.forEach((value, index) => {
                // if-statement to check if currently-iterated variable is empty
                if (value === '') {
                    // set the value of said empty variable as null
                    debtor_array[index] = null;
                }
            });

            // use fetch() function to send stored values to Flask for data processing
            fetch(`/debtor-processor`, {
                // notify Flask that the request being made uses POST method
                method: 'POST',

                // notify Flask that the data being sent along with the request is in json format
                headers: {
                    'Content-Type': 'application/json',
                },

                // use json.stringify() function to compile required data into json before sending it to Flask
                body: JSON.stringify({
                    debtor_name: debtor_name,
                    debtor_age: debtor_array[0],
                    debtor_address: debtor_array[1],
                    debtor_phone: debtor_array[2]
                })
            })
                
                // receive the returned json result by Flask
                .then(response => response.json())

                // extract the values of said json result
                .then(data => {
                    // call show_toast() function for notification processing
                    show_toast(data.type, data.msg);

                    // clear the respective input fields after submission
                    document.getElementById('debtor_name').value = '';
                    document.getElementById('debtor_age').value = '';
                    document.getElementById('debtor_address').value = '';
                    document.getElementById('debtor_phone').value = '';

                    // disable debtor button after submission
                    document.getElementById('debtor_submit').disabled = true;
                });
            
            // end this switch if matched
            break;

        // if the button clicked is that of debt_input
        case 'debt_input':
            // store the submitted values in their respective variables
            let debt_name = document.getElementById('debt_name').value;
            let debt_date = document.getElementById('debt_date').value;
            let debt_amount = document.getElementById('debt_amount').value;
            let debt_percent = document.getElementById('debt_percent').value;
            let debt_interest = document.getElementById('debt_interest').value;
            let debt_total = document.getElementById('debt_total').value;

            // use fetch() function to send stored values to Flask for data processing
            fetch(`/debt-processor`, {
                // notify Flask that the request being made uses POST method
                method: 'POST',

                // notify Flask that the data being sent along with the rquest is in json format
                headers: {
                    'Content-Type': 'application/json',
                },

                // use json.stringify() function to compile required data into json before sending it to Flask
                body: JSON.stringify({
                    debt_name: debt_name,
                    debt_date: debt_date,
                    debt_amount: debt_amount,
                    debt_percent: debt_percent,
                    debt_interest: debt_interest,
                    debt_total: debt_total
                })
            })
                
                // receive the returned json result by Flask
                .then(response => response.json())

                // extract the values of said json result
                .then(data => {
                    // call show_toast() function for notification processing
                    show_toast(data.type, data.msg);

                    // clear the respective input fields after submission
                    document.getElementById('debt_name').value = '';
                    document.getElementById('debt_date').value = '';
                    document.getElementById('debt_amount').value = '';
                    document.getElementById('debt_percent').value = '';
                    document.getElementById('debt_interest').value = '';
                    document.getElementById('debt_total').value = '';

                    // disable debt button after submission
                    document.getElementById('debt_submit').disabled = true;
                });
            
            // end this switch if matched
            break;

        // if the button clicked is that of payment_input
        case 'payment_input':
            // store the submitted values in their respective variables
            let pay_name = document.getElementById('pay_name').value;
            let pay_date = document.getElementById('pay_date').value;
            let pay_principal = document.getElementById('pay_principal').value;
            let pay_interest = document.getElementById('pay_interest').value;
            let pay_total = document.getElementById('pay_total').value;

            // use fetch() function to send stored values to Flask for data processing
            fetch(`/payment-processor`, {
                // notify Flask that the request being made uses POST method
                method: 'POST',

                // notify Flask that the data being sent along with the request is in json format
                headers: {
                    'Content-Type': 'application/json',
                },

                // use json.stringify() function to compile required data into json before sending it to Flask
                body: JSON.stringify({
                    pay_name: pay_name,
                    pay_date: pay_date,
                    pay_principal: pay_principal,
                    pay_interest: pay_interest,
                    pay_total: pay_total
                })
            })
                
                // receive the returned json result by Flask
                .then(response => response.json())

                // extract the values of said json result
                .then(data => {
                    // call show_toast() function for notification processing
                    show_toast(data.type, data.msg);

                    // clear the respective input fields after submission
                    document.getElementById('pay_name').value = '';
                    document.getElementById('pay_date').value = '';
                    document.getElementById('pay_principal').value = '';
                    document.getElementById('pay_interest').value = '';
                    document.getElementById('pay_total').value = '';

                    // disable payment button after submission
                    document.getElementById('pay_submit').disabled = true;
                });
            
            // end this switch if matched
            break;

        // if the button clicked is that of view_history
        case 'view_history':
            // clear old data from history_table and hist_balance before updating it
            history_table.innerHTML = '';
            hist_balance.value = '';

            // store the submitted values in their respective variables
            let hist_name = document.getElementById('hist_name').value;

            // initialize an empty variable to store hist_type
            let hist_type;
            
            // store all radio buttons of a specific name in a variable
            let radio_buttons = document.getElementsByName('hist_type');

            // use forEach() function to loop through all buttons
            radio_buttons.forEach(button => {
                // if currently-iterated radio button is checked
                if (button.checked) {
                    // store the active radio button's value in the initialized variable
                    hist_type = button.value;
                }

                // disable currently-iterated radio button
                button.checked = false;
            });

            // use fetch() function to send stored values to Flask for data processing
            fetch(`/history-processor`, {
                // notify Flask that the request being made uses POST method
                method: 'POST',

                // notify Flask that the data being sent along with the request is in json format
                headers: {
                    'Content-Type': 'application/json',
                },

                // use json.stringify() function to compile required data into json before sending it to Flask
                body: JSON.stringify({
                    hist_name: hist_name,
                    hist_type: hist_type
                })
            })
                
                // receive the returned json result by Flask
                .then(response => response.json())

                // extract the values of said json result
                .then(data => {
                    // if-condition to check if three of the returned required values contain something
                    if (data.headerlist !== null && data.datarows !== null && data.balance !== null) {
                        // call table_generator() function for history table generation
                        table_generator(data.headerlist, data.datarows);

                        // fill the respective input fields after submission
                        hist_balance.value = data.balance;
                    }

                    // call show_toast() function for notification processing
                    show_toast(data.type, data.msg);

                    // clear the respective input fields after submission
                    document.getElementById('hist_name').value = '';

                    // disable history button after submission
                    document.getElementById('hist_submit').disabled = true;
                });
            
            // end this switch if matched
            break;
    }
}