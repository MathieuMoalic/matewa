<script lang="ts">
    import { onMount } from "svelte";
    import { getRandomWord } from "../api/crud";
    let word = { en: "", pl: "", fr: "" };
    let input_word = "";
    onMount(async () => {
        const res = await getRandomWord();
        word = res;
    });
    let checkWord = () => {
        if (input_word === word.pl) {
            console.log("correct");
        } else {
            console.log("incorrect");
        }
    };
</script>

<main>
    <div>Translate 🇫🇷 '{word.fr}' in 🇵🇱 ({word.pl})</div>
    <input
        bind:value={input_word}
        placeholder="Translate 🇫🇷 '{word.fr}' in 🇵🇱 "
    />
    <button
        type="submit"
        on:click|preventDefault={checkWord}
        class="btn btn-primary">Check</button
    >
</main>
