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

// store all forms to their respective variables
let debtor_form = document.getElementById('debtor_form');
let debt_form = document.getElementById('debt_form');
let payment_form = document.getElementById('payment_form');
let history_form = document.getElementById('history_form');

// create a function to check if the input fields of a form are filled or not
function check_form(formId) {
    // retrieve the form elements using provided formId
    let form = document.getElementById(formId);

    // retrieve submit button within the form
    let submitButton = form.querySelector('button[type="submit"]');

    // check if all input fields meet their respective attribute requirements
    let isFormValid = Array.from(form.elements).every(element => {
        // for each element in the form, check if it's an input element, and if it meets its attribute requirements
        return element.tagName.toLowerCase() !== 'input' || element.checkValidity();
    });

    // disable submit button if form is invalid
    submitButton.disabled = !isFormValid;
}

// call check_form() function to monitor validity of debtor_form, debt_form, payment_form, and history_form in real time
debtor_form.addEventListener('input', () => check_form('debtor_form'));
debt_form.addEventListener('input', () => check_form('debt_form'));
payment_form.addEventListener('input', () => check_form('payment_form'));
history_form.addEventListener('input', () => check_form('history_form'));