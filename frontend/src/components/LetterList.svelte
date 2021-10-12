<script lang="ts">
    import { Button, Col, Container, Row, Badge } from "sveltestrap";
    import { shuffled_word, input_word, word } from "../store";
    import LetterButton from "./LetterButton.svelte";
    type ButtonColor = "primary";
    let color: ButtonColor = "primary";
    $shuffled_word = $word.pl
        .split("")
        .sort(function () {
            return 0.5 - Math.random();
        })
        .join("");
    let addLetter = (letter: string) => {
        $input_word += letter;
    };
    let removeLetter = () => {
        $input_word = $input_word.slice(0, $input_word.length - 1);
    };
    let clearInput = () => {
        $input_word = "";
    };
</script>

<Row>
    {#each $shuffled_word as char}
        <Col>
            <LetterButton
                addLetter={function () {
                    addLetter(char);
                }}
                {char}
            />
        </Col>
    {/each}
</Row>
<Row>
    <Col>
        <Button
            on:click={function () {
                removeLetter();
            }}
            {color}
        >
            Remove
        </Button>
    </Col>
    <Col>
        <Button
            on:click={function () {
                clearInput();
            }}
            {color}
        >
            Clear
        </Button>
    </Col>
</Row>
