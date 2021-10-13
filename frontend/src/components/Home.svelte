<script lang="ts">
    export let currentPage: string;
</script>

<main>
    <button class="default" on:click={() => (currentPage = "play")}>Play</button
    >
    <button class="default" on:click={() => (currentPage = "addWord")}
        >Add Word</button
    >
    <button class="default" on:click={() => (currentPage = "listWords")}
        >Words</button
    >
</main>
