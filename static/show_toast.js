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

// store toast_box container to a variable
let toast_box = document.getElementById('toast_box');

// create a function that will handle toast notification display generation
function show_toast(type, msg) {
    // create a new div element and store it in a variable
    let toast = document.createElement('div');

    // set a css class to newly-created div
    toast.classList.add('toast', type);

    // set a text message in said div class
    toast.innerHTML = msg;
    
    // append newly-created div in toast_box container
    toast_box.appendChild(toast);

    // set a timeout to make toast disappear after 5000 milliseconds (5 seconds)
    setTimeout(() => {
        toast.remove();
    }, 5000);
}