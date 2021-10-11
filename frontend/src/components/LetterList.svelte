<script lang="ts">
    import { Button, Col, Container, Row, Badge } from "sveltestrap";
    import { shuffled_word, word, input_word } from "../store";
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
    console.log($word);
</script>

<Row>
    {#each $shuffled_word as letter}
        <Col>
            <Button
                outline
                on:click={function () {
                    addLetter(letter);
                }}
                {color}>{letter}</Button
            >
        </Col>
    {/each}
</Row>
{#each $input_word as letter}
    <Badge>{letter}</Badge>
{/each}
