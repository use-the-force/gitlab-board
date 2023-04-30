<script>
    import { onMount } from "svelte";
    import {
        projects,
        teamprojects,
        members,
        issues,
        statuses, statusesNameIds,
        priorities,
        types,
        labels,
        teams,
        displaymode,
        activeProjectFilter
    } from "../../store";
    import { getAllProjectsIssues, getAllProjectsMembers, getAllProjectsLabels, getProjects } from "../../api/gitlab";
    import { getTeams, getTeamProjects } from "../../api/board";
    import {
        Container,
        Styles,
        Offcanvas,
    } from "sveltestrap";
    import UserBoard from "../board/UserBoard.svelte"
    import SubNav from "../SubNav.svelte";
    import Settings from "../settings/Settings.svelte";
    import Navbar from "../layout/Navbar.svelte";
    import Footer from "../layout/Footer.svelte";
    import Loading from "../layout/Loading.svelte";

    let showBoardSettings = false;
    let showLoading = true;

    const toggleBoardSettings = () => {
        showBoardSettings = !showBoardSettings;
    }

    const editBoardClick = () => {
        toggleBoardSettings();
    }

    const initTeams = async () => {
        const res = await getTeams();
        const json_res = await res.json();

        $teams = json_res.data;
        $activeProjectFilter = $teams[0].id;
    }

    const initTeamProjects = async () => {
        $projects = await getProjects();

        for (let t of $teams) {
            const res = await getTeamProjects(t.id);
            const json_res = await res.json();

            $teamprojects[t.id] = json_res.data.map(p => p.gitlab_project_id);
        }
    }

    const initLabels = async () => {
        let labels = await getAllProjectsLabels($projects.map(({id}) => id));
        let uniqLabels = [...new Map(labels.map((i) => [i.id, i])).values()];
        console.log(">>> uniqLabels", uniqLabels);

        $statuses = uniqLabels.filter(i => i.name.indexOf("Status::") == 0).sort((a, b) => a.name.localeCompare(b.name));
        $priorities = uniqLabels.filter(i => i.name.indexOf("Priority::") == 0);
        $types = uniqLabels.filter(i => i.name.indexOf("Type::") == 0);
        
        for (let s of $statuses) {
            if (!$statusesNameIds[s.name]) {
                $statusesNameIds[s.name] = [];
            }

            $statusesNameIds[s.name].push(s.id);
        }
    }

    onMount(async () => {
        await initTeams();
        await initTeamProjects();
        await initLabels();

        for (let l of [...$types, ...$statuses, ...$priorities]) {
            $labels[l["name"]] = l;
        }

        console.log(">>> statuses", $statuses)

        $members = await getAllProjectsMembers($projects.map(({id}) => id));
        $members = [...$members, {name: "No Assignee", id: null}].sort((a, b) => a.name.localeCompare(b.name));
        $issues = await getAllProjectsIssues($projects.map(({id}) => id));
        showLoading = false;
    });
</script>

<Styles/>

<Navbar></Navbar>

<SubNav on:editBoardClick={editBoardClick} on:kanbanModeEnabled={() => {$displaymode="kanban"}}
        on:listModeEnabled={() => {$displaymode="list"}}></SubNav>

<Offcanvas isOpen={showBoardSettings} toggle={toggleBoardSettings} placement="end" scroll style="width: 50vw;">
    <Settings/>
    <!-- {#each $statuses as status, index (status.name)}
        <div>
        {status.name}
        </div>
    {/each} -->
</Offcanvas>

<!-- <Offcanvas isOpen={columnSettingsOpen} toggle={toggleColumnSettings} placement="end" scroll style="width: 30vw;">
  {#each $statuses as status, index (status.name)}
    <div animate:flip
      draggable={true}
      on:dragstart={event => dragstart(event, index)}
      on:drop|preventDefault={event => drop(event, index)}
      on:dragover={() => {return false}}
      on:dragenter={() => hovering = index}>
      {status.name}
    </div>
  {/each}
</Offcanvas> -->


<Container fluid class="py-4 bg-white">
    <div>
        {#if showLoading}
            <div class="loading">
                <div>
                    <Loading></Loading>
                    <h4 class="text-center">Configuring board</h4>
                    <p class="text-center text-secondary">It may take a while...</p>
                </div>
            </div>
        {:else}
            {#each $members as member (member.id)}
                <UserBoard {member}></UserBoard>
            {/each}
        {/if}
    </div>
</Container>

<Footer></Footer>

<style>
    h4:focus-visible {
        outline: none;
    }

    .loading {
        height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
