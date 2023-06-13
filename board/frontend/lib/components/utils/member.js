export const getMemberAvatar = (member) => {
    if (member && member.avatar_url) {
        return member.avatar_url;
    }

    return `${global.BOARD_SUBPATH}/images/no-avatar.jpg`;
};
