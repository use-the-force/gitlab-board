import { get } from "svelte/store";
import { statuses } from "../../store";

export const getLabelNameById = (id) => {
    const sstatuses = get(statuses);
    return sstatuses.filter(s => s.id === id)[0].name;
};

export const getLabels = (labels) => {
    // Returns every label which is not Type:: Proirity:: and Status:: label
    return labels.filter(e => !e.includes("Type::") && !e.includes("Priority::") && !e.includes("Status::"));
};

export const getPriorityLabel = (labels) => {
    const l = labels.filter(e => e.includes("Priority::"));

    if (l) {
        return l[0];
    } else {
        return null;
    }
};

export const extractStatusLabel = (labels) => {
    return labels.filter(e => e.includes("Status::"));
};


export const getUniqLabelNamesByIds = (label_ids) => {
    const label_names = label_ids.map(id => getLabelNameById(id));
    return [...new Set(label_names)];
}
