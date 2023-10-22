import { writable, readable } from "svelte/store";

export const loadingBoardInfo = writable("Loading...");
export let authorized = writable(false);

const storedSettingsMergeRequests = localStorage.getItem("settingsMergeRequests")
export const settingsMergeRequests = writable(storedSettingsMergeRequests);
settingsMergeRequests.subscribe(val => {
    localStorage.setItem("settingsMergeRequests", val);
})

export const projects = writable([]);
export const teamprojects = writable({});
export const issues = writable([]);
export const members = writable([]);
export const teams = writable([]);
export const statuses = writable([]);
export const statusesNameIds = writable({});
export const priorities = writable([]);
export const types = writable([]);
export const labels = writable([]);
export const activeProjectFilter = writable(null);

// TODO: i18n
export const defaultType = readable({
    color: "#2673bf",
    description: "Задача",
    name: "Type::Task",
    text_color: "#FFFFFF"
});

export const setAuthorized = (value) => {
    authorized = value;
};

export const displaymode = writable("kanban");
