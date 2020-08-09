import React,{Component} from "react";


class User extends Component{
    constructor(props) {
        super(props);
        this.state={
            isMute: false,
            user: this.props.user
        };
        this.updateState = this.updateState.bind(this);
      }

      updateState(){
          this.setState({
            isMute: !this.state.isMute
          });
      }


    render(){
        return(
            <tr>
                {this.state.isMute? 
                <td style={{textDecoration:"line-through"}}>{this.props.user}</td>:<td>{this.props.user}</td>}
                {this.state.isMute? 
                <td><button onClick={()=> {this.updateState(), this.props.unmute(this.props.user)}}>UnMute</button></td>: 
                <td><button onClick = {()=> {this.updateState(), this.props.mute(this.props.user)}}>Mute</button></td>}
                
            </tr>
        );
    }
}

export default User;