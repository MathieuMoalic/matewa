<script lang="ts">
    import { onMount } from "svelte";
    import { Progress } from "sveltestrap";
    import { getRandomWord } from "../api/crud";
    let word = { en: "", pl: "", fr: "" };
    let input_word = { en: "", pl: "", fr: "" };
    onMount(async () => {
        const res = await getRandomWord();
        word = res;
    });
    let checkWord = () => {
        if (input_word.en === word.en) {
            console.log("correct");
        } else {
            console.log("incorrect");
        }
    };
    let timeLeft = 100;
    let id = setInterval(updateProgressBar, 100);
    function updateProgressBar() {
        if (timeLeft == 0) {
            clearInterval(id);
        } else {
            timeLeft--;
        }
    }
</script>

<main>
    <Progress animated color="success" value={timeLeft} />
    <h1>Words</h1>
    <div>Word in English :{word.en}</div>
    <div>Word in Polish :{word.pl}</div>
    <div>Word in French :{word.fr}</div>
    <input bind:value={input_word.en} placeholder="Word in English" />
    <input bind:value={input_word.pl} placeholder="Word in Polish" />
    <input bind:value={input_word.fr} placeholder="Word in French" />
    <button
        type="submit"
        on:click|preventDefault={checkWord}
        class="btn btn-primary">checkWord</button
    >
</main>
