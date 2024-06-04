<script lang='ts'>
    import { goto } from '$app/navigation';
    import TailwindCSS from '/Users/zakkilpatrick/Desktop/Sveltekit/MagicWeb/src/lib/TailwindCSS.svelte'
    import { createClient } from '@supabase/supabase-js';

    const supabase= createClient(
    // process.env.NEXT_PUBLIC_PROJECT_URL as string,
    // process.env.NEXT_PUBLIC_SUPABASE_KEY as string
    "https://qbnoafpfqzaokvexhsoy.supabase.co",
    

    );

    let username =''
    let password = ''

    async function handleSignup(username: string, password: string): Promise<void> {
    const { data, error } = await supabase.auth.signUp({
    email: username,
    password: password,
    options: {
      emailRedirectTo: 'https://example.com/welcome',
    },
  });
}

async function handleLogIn(username: string, password: string) {
  const { data, error } = await supabase.auth.signInWithPassword({
    email: username,
    password: password,
  })
}


</script>

<link href="./src/app.css" rel="stylesheet">

<TailwindCSS />

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

    <div>Please sign in or sign up</div>
    <input bind:value={username} type="text" id="username" name="username">
    <input bind:value={password} type="text" id="password" name="password">
    <button on:click={() => {handleSignup(username, password)}}>Sign in</button>
    <button on:click={() => {handleLogIn(username, password)}}>Log in</button>
</main>
