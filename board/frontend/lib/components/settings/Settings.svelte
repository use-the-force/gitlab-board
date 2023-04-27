<script>
    import { TabContent, TabPane } from "sveltestrap";
    import TeamColumns from "../board/team/TeamColumns.svelte";
    import TeamList from "../board/team/TeamList.svelte";
</script>

<TabContent>
    <TabPane tabId="teams" tab="Teams" active>
        <TeamList />
    </TabPane>
    <TabPane tabId="columns" tab="Team Columns" class="mt-4">
        <TeamColumns />
    </TabPane>
</TabContent>
