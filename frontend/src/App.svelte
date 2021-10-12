<script lang="ts">
	import { Styles } from "sveltestrap";
	import AddWord from "./components/AddWord.svelte";
	import Navbar from "./components/Navbar.svelte";
	import Home from "./components/Home.svelte";
	import Play from "./components/Play.svelte";
	import ListWords from "./components/ListWords.svelte";

	let currentTab = "home";
</script>

<Styles />

<body>
	<Navbar bind:currentTab />
	{#if "home" === currentTab}
		<!-- <Home /> -->
		<Play />
	{/if}
	{#if "addWord" === currentTab}
		<AddWord />
	{/if}
	{#if "play" === currentTab}
		<Play />
	{/if}
	{#if "listWords" === currentTab}
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
	}
	:global(body) {
		margin: 0px;
		border: 0px;
		padding: 0px;
	}
	body {
		background-color: rgb(7, 60, 78);
		font-size: 48px;
	}
</style>
