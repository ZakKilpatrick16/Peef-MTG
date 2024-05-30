<script>
    import { goto } from '$app/navigation';
</script>

<style>
    main {
        text-align: center;
        margin-top: 50px;
    }
</style>

<main>
    <h2>Welcome to Page 1!</h2>
    <p>This is the detail page for Name 1.</p>
    <button on:click={() => goto('/')}>Go back to Home</button>
</main>
