<script>
    import {beforeUpdate} from "svelte";
    import {Accordion, AccordionItem, InputGroup, Input, Form, Button} from "sveltestrap";
    import {teams, statuses, statusesNameIds} from "../../../store";
    import {addTeamColumn, deleteTeamColumn, attachTeamColumnStatus, detachTeamColumnStatus} from "../../../api/board";

    let addTeamColumnName = "";
    let addTeamColumnTeamId = null;
    let addTeamColumnColor = "#dee2e6";

    const handleAddColumn = async (e) => {
        e.preventDefault();
        const res = await addTeamColumn(addTeamColumnTeamId, addTeamColumnName, addTeamColumnColor);

        if (res.ok) {
            const teamIndex = $teams.findIndex(t => {
                return t.id === addTeamColumnTeamId;
            });
            const json_res = await res.json();

            $teams[teamIndex].columns.push(json_res.data);
            $teams = $teams;
            console.log("handleAddColumn", $teams);
            addTeamColumnName = "";
        }
    }

    const handleDeleteColumn = async (team_id, column_id) => {
        const res = await deleteTeamColumn(team_id, column_id);

        if (res.ok) {
            const teamIndex = $teams.findIndex(t => {
                return t.id === team_id;
            });
            const columnIndex = $teams[teamIndex].columns.indexOf(column_id);

            $teams[teamIndex].columns.splice(columnIndex, 1);
            $teams = $teams;
        }
    }

    const handleCheckTeamColumn = async (team_id, column_id, status_ids, e) => {
        for (let status_id of status_ids) {
            if (e.target.checked) {
                const res = await attachTeamColumnStatus(team_id, column_id, status_id);

                if (res.ok) {
                    const teamIndex = $teams.findIndex(t => {
                        return t.id === team_id;
                    });
                    const columnIndex = $teams[teamIndex].columns.findIndex(t => {
                        return t.id === column_id;
                    });

                    $teams[teamIndex].columns[columnIndex].gitlab_label_ids.push(status_id);
                    $teams = $teams;
                }
            } else {
                const res = await detachTeamColumnStatus(team_id, column_id, status_id);

                if (res.ok) {
                    const teamIndex = $teams.findIndex(t => {
                        return t.id === team_id;
                    });
                    const columnIndex = $teams[teamIndex].columns.findIndex(t => {
                        return t.id === column_id;
                    });
                    const statusIndex = $teams[teamIndex].columns[columnIndex].gitlab_label_ids.indexOf(status_id);

                    $teams[teamIndex].columns[columnIndex].gitlab_label_ids.splice(statusIndex, 1);
                    $teams = $teams;
                }
            }
        }
    }

    const teamColumnHasStatus = (team_id, column_id, status_ids) => {
        const team = $teams.filter(t => t.id == team_id)[0];
        const column = team.columns.filter(c => c.id == column_id)[0];
        return column.gitlab_label_ids.filter(x => status_ids.includes(x)).length > 0;
    }

    beforeUpdate(async () => {
        if ($teams.length > 0 && !addTeamColumnTeamId) {
            addTeamColumnTeamId = $teams[0].id;
        }
    });
</script>

<Form class="my-4" on:submit={e => handleAddColumn(e)}>
    <InputGroup>
        <Input placeholder="Column name" bind:value={addTeamColumnName}/>
        <Input type="color" class="color" bind:value={addTeamColumnColor}/>
        <select bind:value={addTeamColumnTeamId} class="form-select form-select-sm">
            {#each $teams as t (t.id)}
                <option value={t.id}>{t.name}</option>
            {/each}
        </select>
        <Button color="primary" on:click={e => handleAddColumn(e)}>Add</Button>
    </InputGroup>
</Form>

<Accordion>
    {#each $teams as t (t.id)}
        <AccordionItem header={t.name}>
            {#each t.columns as c (c.id)}
                <div class="card mb-3">
                    <div class="card-header">
                        {c.name}
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col">
                                <!--
                                <div class="float-start">
                                    <Input type="color" class="color" value={c.color}/>
                                </div>
                                <div class="float-start mx-2">
                                    <Button size="md" color="secondary" class="btn-edit-column">
                                        <span class="bi bi-pen"></span>
                                    </Button>
                                </div>
                                <div class="float-start">

                                <Button size="md" color="danger" class="d-inline-block"
                                        on:click={e => handleDeleteColumn(t.id, c.id)}>
                                    <span class="bi bi-trash"></span>
                                </Button>
                                </div>
                                -->
                                <Button size="md" color="danger" class="d-inline-block"
                                        on:click={e => handleDeleteColumn(t.id, c.id)}>
                                    <span class="bi bi-trash"></span>
                                </Button>
                            </div>
                            <div class="col">
                                {#each [...new Map($statuses.map((i) => [i.name, i])).values()] as s}
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" id="{c.id}-{s.name}-Checkbox"
                                               on:change={(e) => handleCheckTeamColumn(t.id, c.id, $statusesNameIds[s.name], e)}
                                               checked={teamColumnHasStatus(t.id, c.id, $statusesNameIds[s.name])}/>
                                        <label class="form-check-label" for="{c.id}-{s.name}-Checkbox">
                                            {s.name}
                                            <!-- {$statusesNameIds[s.name]} -->
                                        </label>
                                    </div>
                                {/each}
                            </div>
                        </div>
                    </div>
                </div>
            {/each}
        </AccordionItem>
    {/each}
</Accordion>


<style global>
    h5 {
        margin-top: 30px;
    }

    .colname {
        width: 250px;
    }

    .colname-wrap {
        display: flex;
        vertical-align: middle;
        width: 100%;
    }

    :global(.color) {
        -webkit-appearance: none !important;
        width: 42px !important;
        flex-grow: 0 !important;
    }

    :global(.color::-webkit-color-swatch-wrapper) {
        padding: 0 !important;
    }

    :global(.color::-webkit-color-swatch) {
        border: none !important;
    }

    :global(.colname-wrap .btn) {
        margin-left: 5px;
        width: 32px;
        height: 32px;
    }

    :global(.colname-wrap input) {
        margin-left: 5px;
    }

    :global(.colname-wrap .color) {
        margin-left: auto;
        height: 32px;
        width: 32px;
        padding: 0;
        border: 0;
    }

    .btn-edit-column {
        margin-left: .5rem;
        margin-right: .5rem;
    }

</style>
