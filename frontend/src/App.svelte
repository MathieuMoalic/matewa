<script lang="ts">
	import { Styles } from "sveltestrap";
	import AddWord from "./components/AddWord.svelte";
	import Home from "./components/Home.svelte";
	import Play from "./components/Play.svelte";
	import ListWords from "./components/ListWords.svelte";

	let currentPage = "play";
</script>

<Styles />

<body>
	{#if "home" == currentPage}
		<Home bind:currentPage />
	{:else if "addWord" == currentPage}
		<AddWord bind:currentPage />
	{:else if "play" == currentPage}
		<Play />
	{:else if "listWords" == currentPage}
		<ListWords />
	{/if}
</body>

<style>
	:root {
		--c1: hsl(45, 88%, 58%);
		--c2: hsl(45, 85%, 65%);
		--c3: hsl(39, 89%, 53%);
		--c4: hsl(33, 50%, 50%);
		--c5: hsl(27, 30%, 79%);
		font-size: 24px;
	}
	:global(body) {
		margin: 0px;
		border: 0px;
		padding: 0px;
	}
	body {
		background-color: var(--c4);
		font-size: 48px;
	}
	:global(main) {
		align-content: center;
		text-align: center;
	}
	:global(button.default) {
		color: var(--c4);
		background-color: var(--c1);
		width: 75%;
		margin: 1rem;
		border-width: 2px;
		border-color: var(--c2);
		border-radius: 1rem;
	}
</style>
