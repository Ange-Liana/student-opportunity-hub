console.log("script.js loaded");

document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            console.log("FORM SUBMITTED");

        });

    }

});