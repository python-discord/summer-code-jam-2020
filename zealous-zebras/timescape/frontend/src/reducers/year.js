const yearReducer = (state = 2018, action) => {
    switch (action.type) {
        case "SET_YEAR":
            return action.payload
        default:
            return state
    }
}

export default yearReducer;