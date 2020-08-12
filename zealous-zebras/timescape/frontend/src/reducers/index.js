import { combineReducers } from "redux";
import yearReducer from "./year";

export default combineReducers({
    year: yearReducer,
});
