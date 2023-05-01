<!-- <svelte:options accessors/> -->

<script>
    import IssueType from "./IssueType.svelte";
    import PriorityLabel from "../PriorityLabel.svelte";
    import { extractStatusLabel, getPriorityLabel, getUniqLabelNamesByIds } from "../utils/labels";
    import { getTeamColumns } from "../utils/columns";
    import { teams, issues } from "../../store";
    import { updateIssueLabels } from "../../api/gitlab";

    export let col;
    export let displayedIssues = [];

    $: doGetTeamColumns = () => {
        $teams; // reactivity crutch
        return getTeamColumns();
    }

    export const getIssuesCount = () => {
        return displayedIssues.length;
    }

    const handleChangeIssueStatus = async (status_label_name, issue) => {
        const status_label_to_remove = extractStatusLabel(issue.labels);
        const new_labels_list = [...issue.labels.filter(x => !status_label_to_remove.includes(x)), status_label_name];

        try {
            await updateIssueLabels(issue.project_id, issue.iid, new_labels_list);
            const sissue_index = $issues.findIndex(i => {
                return i.iid === issue.iid && i.project_id == issue.project_id;
            });
            $issues[sissue_index].labels = new_labels_list;
            $issues[sissue_index].changed = true; //temporary, just to highlight changed issues
            $issues;
        } catch (e) {
        }

    }
</script>

{#if displayedIssues.length > 0}
    <div class="container-fluid mt-2">
        <table class="table table-bordered rounded rounded-1 overflow-hidden" style="margin: 5px">
            <thead>
            <tr>
                <th>Status</th>
                <th>Project</th>
                <th>Priority</th>
                <th>Issue</th>
            </tr>
            </thead>
            <tbody>
            {#each displayedIssues as iss (iss.id)}
                <tr class={iss.changed ? "changed" : ""}>
                    <td class="status">
                        <select class="form-select form-select-sm"
                                on:change={e => {handleChangeIssueStatus(e.target.value, iss)}}>
                            {#each doGetTeamColumns() as c, ci}
                                <optgroup label={c.name}>
                                    {#each getUniqLabelNamesByIds(c.gitlab_label_ids) as label}
                                        <option
                                                selected={c.name == col.name && extractStatusLabel(iss.labels) == label}
                                                value={label}>
                                            {label}
                                        </option>
                                    {/each}
                                </optgroup>
                            {/each}
                        </select>
                    </td>
                    <td class="project">
                        {iss.references.full}
                    </td>
                    <td class="priority">
                        {#if getPriorityLabel(iss.labels)}
                            <PriorityLabel label={getPriorityLabel(iss.labels)}/>
                        {/if}
                    </td>
                    <td class="issue">
                        <IssueType labels={iss.labels}></IssueType>
                        <a href="{iss.web_url}" target="_blank" rel="noreferrer">{iss.title}</a>
                        {#if iss.milestone}
                    <span class="milestone">
                        <i class="bi bi-tag-fill"></i> 
                        <a href="{iss.milestone.web_url}" target="_blank" rel="noreferrer">{iss.milestone.title}</a>
                    </span>
                        {/if}
                    </td>
                </tr>
            {/each}
            </tbody>
        </table>
    </div>
{/if}


<style>
    table {
        font-size: 14px;
        margin: 0 0 20px 0 !important;
    }

    h4 {
    }

    th {
    }

    .status {
        width: 350px;
    }

    .project {
        width: 300px;
    }

    .priority {
        width: 150px;
    }

    :global(.priority .badge) {
        margin-top: 0 !important;
    }

    .milestone {
        margin-left: .25rem;
    }

    .milestone a {
        font-size: .8rem;
        color: #9d9d9d;
        position: relative;
        top: .05rem;
        font-weight: 500;
    }

    .milestone i {
        position:relative;
        top: .05rem;
        color: #9d9d9d;
    }

    .issue a {
        text-decoration: none;
    }

    .issue a:hover {
        text-decoration: underline;
    }

    .changed {
        background-color: #ffffee;
    }
</style>
