<!-- <svelte:options accessors/> -->

<script>
    import Label from "./Label.svelte";
    import {Card, CardBody, CardFooter} from "sveltestrap";
    import IssueType from "./IssueType.svelte";
    import PriorityLabel from "../PriorityLabel.svelte";
    import {getLabels, getPriorityLabel} from "../utils/labels";

    export let closed = false;
    export let col;
    export let issues = [];

    export const toggleColumn = () => {
        closed = !closed;
    }

    export const getIssuesCount = () => {
        return issues.length;
    }
</script>

{#if closed }
    <div class="card mx-3 my-2 p-0 closed-column">
        <div class="card-header">
            <div class="card-color" style="border-color: {col.color}"></div>
            <div class="card-chevron d-inline" on:click={(e) => toggleColumn(e)}>
                <i class="bi bi-chevron-left"></i>
            </div>
        </div>
        <div class="card-body">
            <span>{col.name} <i class="bi bi-files"></i> {issues.length}</span>
        </div>
    </div>
{:else}
    <div class="card mx-3 my-2 p-0">
        <div class="card-header">
            <div class="card-color" style="border-color: {col.color}"></div>
            <div class="card-chevron d-inline" on:click={(e) => toggleColumn(e)}>
                <i class="bi bi-chevron-right"></i>
            </div>

            {col.name}

            <div class="issue-count">
                <i class="bi bi-files"></i> {issues.length}
            </div>
        </div>
        <div class="card-body">
            {#each issues as i (i.id)}
                <Card class="mb-3">
                    <CardBody>
                        <h6>
                            <IssueType labels={i.labels}></IssueType>
                            <a href="{i.web_url}" target="_blank">{i.title}</a>
                        </h6>

                        <div>
                            {#if getPriorityLabel(i.labels)}
                                <PriorityLabel label={getPriorityLabel(i.labels)}/>
                            {/if}

                            {#if i.milestone}
                                <span class="milestone">
                                    <i class="bi bi-tag-fill"></i>
                                    <a class="milestone" href="{i.milestone.web_url}" target="_blank">{i.milestone.title}</a>
                                </span>
                            {/if}
                        </div>

                        {#each getLabels(i.labels) as label}
                            <Label {label}/>
                        {/each}
                    </CardBody>
                    <CardFooter>
                        <p>{i.references.full}</p>
                    </CardFooter>
                </Card>
            {/each}
        </div>
    </div>
{/if}

<style>
    h6 {
        font-size: .9rem;
        margin-bottom: 0;
    }

    a {
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    p {
        font-size: .75rem;
        font-weight: 600;
        margin-bottom: 0;
    }

    .bi-files {
        font-size: .9rem;
    }

    .issue-count {
        float: right;
    }

    .card {width: 25rem;}

    .card-header {
        background: #fff;
        padding: .8rem;
        font-size: .8rem;
    }

    .card-body {
        height: 600px;
        overflow-y: scroll;
    }

    .card-color {
        border-top: 3px solid;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        content: '';
        position: absolute;
        width: calc(100% + 2px);
        top: 0;
        left: 0;
        margin-top: -1px;
        margin-right: -1px;
        margin-left: -1px;
        padding-top: 1px;
        padding-right: 1px;
        padding-left: 1px;
    }

    .card-chevron {
        padding: .25rem;
        border-radius: .1rem;
        cursor: pointer;
    }

    .card-chevron:hover {
        background: rgba(0, 0, 0, .1);
    }

    .closed-column {
        width: 3rem !important;
    }

    .closed-column .card-header {
    }

    .closed-column span {
        transform-origin: 0 0;
        transform: rotate(90deg);
        width: 15rem;
        padding: .2rem;
        display: block;
        position: relative;
        left: 1.5rem;
        top: .5rem;
        font-weight: 500;
    }

    .milestone a {
        font-size: .8rem;
        color: #9d9d9d;
        position: relative;
        top: .12rem;
        font-weight: 500;
    }

    .milestone i {
        position:relative;
        top:.23rem;
        color: #9d9d9d;
    }
</style>
