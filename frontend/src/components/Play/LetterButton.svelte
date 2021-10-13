<script lang="ts">
    import { input_word } from "../../store";

    export let char: string;
    let disabled = false;

    function addLetter() {
        $input_word += char;
    }
</script>

<button {disabled} on:click={addLetter}>
    <div>
        {char}
    </div>
</button>

<style>
    div {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    button {
        background-color: var(--c2);
        display: flex;
        vertical-align: middle;
        align-items: center;
        color: var(--c4);
        font-family: sans-serif;

        border: 0.2rem solid var(--c1);
        /* border-radius: 0.5rem; */
        /* border-width: 0.1rem; */
        /* border-color: var(--c3); */

        /* width: 2rem; */
        /* height: 2rem; */
        padding: 0px;
        margin: 0px;
    }
</style>
