<script lang="ts">
    import { onMount } from "svelte";
    let words = [];
    onMount(async () => {
        fetch("http://localhost:8000/words/")
            .then((response) => response.json())
            .then((data) => {
                words = data;
            })
            .catch((error) => {
                console.log(error);
                return [];
            });
    });
</script>

<main>
    <h1>Words</h1>
    <ul>
        {#each words as word}
            <li>{word.en}</li>
        {/each}
    </ul>
</main>
