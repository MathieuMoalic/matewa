<script lang="ts">
    import { onMount } from "svelte";

    import { Icon, Col, Container, Row } from "sveltestrap";

    import { getWordList } from "../api/crud";
    import UpdateWord from "./UpdateWord.svelte";

    let words = [];
    onMount(async () => {
        const res = await getWordList();
        words = res;
    });
</script>

<main>
    <Container>
        {#each words as word}
            <Row>
                <Col xs="1">
                    <UpdateWord {word} />
                </Col>
                <Col xs="auto">🇬🇧 {word.en}</Col>
                <Col xs="auto">🇫🇷 {word.fr}</Col>
                <Col xs="auto">🇵🇱 {word.pl}</Col>
            </Row>
        {/each}
    </Container>
</main>
