export const setYear = (year) => {
    return {
        type: "SET_YEAR",
        payload: year
    }
}
export const getYear = () => {
    return {
        type: "GET_YEAR"
    }
}
