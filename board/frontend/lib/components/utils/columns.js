import { get } from "svelte/store";
import { activeProjectFilter, teams } from "../../store";

export const getTeamColumns = () => {
    const $teams = get(teams);
    const $activeProjectFilter = get(activeProjectFilter);
    const team = $teams.filter(t => t.id === $activeProjectFilter)[0];

    if (team?.columns) {
        return team.columns;
    } else {
        return [];
    }
};

export const getTeamColumnNameByLabelId = (id, label) => {
    const columns = getTeamColumns();
    console.log(">>> columns", columns, id);
    const find = columns.filter(e => e.gitlab_label_ids.indexOf(id) > -1);

    if (find.length > 0) {
        return find[0].name;
    } else {
        return label;
    }
};
