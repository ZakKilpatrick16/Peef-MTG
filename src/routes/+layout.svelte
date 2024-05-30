<!-- src/routes/+Layout.svelte -->

<style>
    /* Global styles for the layout */
    main {
        text-align: center;
        margin-top: 50px;
    }

    .name-list {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
    }

    .name-button {
        padding: 10px 20px;
        font-size: 16px;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    .name-button:hover {
        background-color: #2980b9;
    }

    .nav-links li a {
    color: #fff; /* Set text color to white */
    text-decoration: none; /* Remove underline from links */
    padding: 5px 10px; /* Add padding to links */
}

.nav-links li a:hover {
    background-color: #555; /* Change background color on hover */
}

</style>



<main>
    <!-- This slot will be replaced with the content of the child components -->
    <slot></slot>
</main>
