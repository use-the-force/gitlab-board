<!-- <svelte:options accessors/> -->

<script>
    import { createEventDispatcher } from "svelte";
    import { activeProjectFilter, teams, displaymode } from "../store.js";

    const dispatch = createEventDispatcher();

    export function switchTeam(value) {
        if (!value) {
            $activeProjectFilter = null;
        } else {
            $activeProjectFilter = parseInt(value);
        }
    }

    const handleEditBoardClick = (e) => {
        e.preventDefault();
        dispatch("editBoardClick");
    }

    const handleKanbanMode = () => {
        dispatch("kanbanModeEnabled");
    }

    const handleListMode = () => {
        dispatch("listModeEnabled");
    }
</script>

<div class="px-4 py-3 border-bottom">
    <form class="row justify-content-end">
        <div class="col">
            <label for="board" class="visually-hidden">Board</label>
            <select class="form-select" id="board" on:change="{(e) => switchTeam(e.target.value)}">
                {#each $teams as t (t.id)}
                    <option value="{t.id}">{t.name}</option>
                {/each}
            </select>
        </div>
        <div class="col">
            <div class="float-end">
                <div class="float-start mx-3">
                    <div class="input-group">
                        <button class="btn btn-outline-secondary {$displaymode == "kanban" ? "active" : ""}" type="button" on:click={handleKanbanMode}>
                            <span class="bi bi-kanban"></span>
                        </button>
                        <button class="btn btn-outline-secondary {$displaymode == "list" ? "active" : ""}" type="button" on:click={handleListMode}>
                            <span class="bi bi-list"></span>
                        </button>
                    </div>
                </div>
                <div class="float-end">
                    <button type="submit" class="btn btn-outline-primary" on:click={e => handleEditBoardClick(e)}>Edit Board</button>
                </div>
            </div>
        </div>

    </form>
</div>

<style>
    form select, form input {
        font-size: .9rem;
    }

    .form-select {
        width: 15rem;
    }

    .input-group-search input, .input-group-search div button {
        height: 2.21rem;
    }
</style>

