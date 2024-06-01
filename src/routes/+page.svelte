<!-- pages.svelte -->

<script lang="ts">
    import { goto } from '$app/navigation';
    import Layout from './+layout.svelte'; // Import the Layout component

    const navigateToPage = (page: string) => {
        goto(`/${page}`);
    };
</script>

<link href="./src/output.css" rel="stylesheet">
<link href="./src/app.css" rel="stylesheet">

<Layout> <!-- Wrap your content with the Layout component -->
    <h1 class="text-6xl font-bold underline">
        Hello world!
      </h1>
    <h2>Welcome to the Home Page!</h2>
    <nav class="navbar">
        <ul class="nav-links">
            <li><a href="/Decks">Decks</a></li>
            <li><a href="/Finance">Finance</a></li>
            <li><a href="/TournamentData">Tournament Data</a></li>
        </ul>
    </nav>
    
</Layout>
