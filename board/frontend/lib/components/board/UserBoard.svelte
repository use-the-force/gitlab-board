<script>
    import IssuesColumn from "./IssuesColumn.svelte";
    import IssuesRow from "./IssuesRow.svelte";
    import {beforeUpdate, afterUpdate} from "svelte";
    import {settings, issues, activeProjectFilter, teamprojects, displaymode, teams} from "../../store";
    import {getLabelNameById} from "../utils/labels";
    import {getTeamColumns} from "../utils/columns";
    import {getMemberAvatar} from "../utils/member";

    export let member;
    let isOpen = false;
    let bindcolumns = [];

    $: cnt = 0;
    $: getIssuesCount = () => {
        let issuesCountSum = 0;

        for (let c of bindcolumns) {
            try {
                issuesCountSum += c.getIssuesCount()
            } catch (e) {
            }
        }

        cnt = issuesCountSum;
    }

    $: doGetTeamColumns = () => {
        $teams; // reactivity crutch
        return getTeamColumns();
    }

    $: getDisplayedIssues = (col) => {
        return $issues.filter(i => {
            if ($teamprojects[$activeProjectFilter].some(f => f == i.project_id)) {
                // Unassigned issues
                if (!i.assignee && !member.id && col.gitlab_label_ids.filter(x => i.labels.includes(getLabelNameById(x))).length > 0) {
                    return i;
                }
                // Assigned issues
                if (i.assignee && i.assignee.id == member.id && col.gitlab_label_ids.filter(x => i.labels.includes(getLabelNameById(x))).length > 0) {
                    return i;
                }

                if ($settings.general.mergeRequests) {
                    // Issues by merge requests
                    if (i.merge_requests.filter(mr => member.id && mr.assignee && mr.assignee.id == member.id).length > 0 && col.gitlab_label_ids.filter(x => i.labels.includes(getLabelNameById(x))).length > 0) {
                        return i;
                    }
                }
            }
        });
    }

    $: getMemberAvatarWrap = (m) => {
        return getMemberAvatar(m)
    }

    beforeUpdate(() => {
        getIssuesCount()
    })

    afterUpdate(() => {
        getIssuesCount()
    })
</script>


<div>
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="assignee {cnt > 0 ? '' : 'hidden'} p-2">
        <span class="assignee-wrap" on:click={() => (isOpen = !isOpen)}>
            <i class="bi {isOpen ? 'bi-chevron-up' : 'bi-chevron-down'}"></i>
            <img class="assignee-avatar" src="{getMemberAvatarWrap(member)}" alt="Assignee Avatar">
            <span class="assignee-name">
                {member.name} ({cnt})
            </span>
        </span>
    </div>
    <div class={isOpen ? "" : "hidden"}>
        {#if $displaymode === "kanban"}
            <div class="row row-cols-4">
                {#each doGetTeamColumns() as col, i}
                    <IssuesColumn {col} issues={getDisplayedIssues(col)} bind:this={bindcolumns[i]}></IssuesColumn>
                {/each}
            </div>
        {:else}
            {#each doGetTeamColumns() as col, i}
                <IssuesRow {col} {member} displayedIssues={getDisplayedIssues(col)} bind:this={bindcolumns[i]}></IssuesRow>
            {/each}
        {/if}
    </div>
</div>

<style>
    img.assignee-avatar {
        width: 1.7rem;
        height: 1.7rem;
        border-radius: 2rem;
        background-size: cover;
        margin: 0 .2rem;
    }

    .row {
        flex-wrap: nowrap;
        width: 100%;
        overflow-x: scroll;
        padding-bottom: 1rem;
    }

    .bi {
        font-size: .6rem;
    }

    .assignee-wrap {
        cursor: pointer;
    }

    .assignee-name {
        font-size: .9rem;
        font-weight: 400;
        margin: 0;
    }

    .assignee-wrap:hover .assignee-name {
        text-decoration: underline;
    }

    .hidden {
        display: none;
    }

    .assignee {
        transition: all .1s linear;
    }
</style>
