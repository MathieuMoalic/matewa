<script lang="ts">
    import { input_word } from "../../store";

    export let char: string;
    let disabled = true;

    function addLetter() {
        $input_word += char;
    }
</script>

<button {disabled} on:click={addLetter}>{char}</button>

<style>
    button {
        background-color: rgb(32, 140, 167);
        vertical-align: middle;
        color: rgb(169, 211, 240);
        font-family: sans-serif;
        font-size: 33px;

        border-radius: 15px;
        border-width: 2px;
        border-color: rgb(169, 211, 240);

        width: 50px;
        height: 50px;
        padding-top: 0px;
        padding-right: 0px;
        padding-bottom: 0px;
        padding-left: 0px;
        margin-top: 0px;
        margin-bottom: 0px;
    }
</style>
