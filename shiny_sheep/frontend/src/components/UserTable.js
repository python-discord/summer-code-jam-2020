import React,{Component} from "react";
import User from "./Users";

class UserTable extends Component{

    constructor(props){
        super(props);
        this.state={
            muteUsers:[],
        }
        this.updateMuteUsers = this.updateMuteUsers.bind(this);
        this.updateUnmuteUser = this.updateUnmuteUser.bind(this);
    }

    updateMuteUsers(user){
        
        let userSet = new Set(this.state.muteUsers);
        userSet.add(user);
        this.setState({
            muteUsers:userSet
        });
        console.log("Muted");
        console.log(this.state.muteUsers);
        
    }

    updateUnmuteUser(user){
        let userSet = new Set(this.state.muteUsers);
        userSet.delete(user);
        this.setState({
            muteUsers:userSet
        });
        console.log("Unmuted")
        console.log(this.state.muteUsers);
    }



    render(){
      
        const rows =[];
        this.props.users.forEach((user) =>{
            rows.push(
                <User user = {user} mute = {this.updateMuteUsers} unmute={this.updateUnmuteUser}/>
            );
        });
        return (
            <table style={{margin:"auto"}}>
                <thead>
                    <tr>
                        <th>Users</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
        );
    }
}

export default UserTable;