import "./CustomContext.css";
import React, { Component } from "react";


class Testing2 extends Component{
    constructor(props) {
        super(props);
        this.state={
            visible: false,
            clicked:false,
            x: 0,
            y: 0,
            };
            this.handleContext = this.handleContext.bind(this);
            this.componentDidMount = this.componentDidMount.bind(this);
    }


    componentDidMount(){
        var self = this;
        addEventListener('click',function(e){
            e.preventDefault();
            self.setState({visible:false, x:0, y:0});
            console.log("Clicking Here");
        });
    }

    componentWillUnmount(){
        document.removeEventListener('click');
    }


    
    
    returnMenu(items){
        var myStyle = {
        position: 'absolute',
        top: `${this.state.y}px`,
        left:`${this.state.x+5}px`
        }
    
        return <div className='custom-context' id='customcontext' style={myStyle}>
            <p>This is a context test</p>
        </div>;
    }
  

    handleContext(){
        event.preventDefault();
        const clickX = event.clientX;
        const clickY = event.clientY;
        this.setState({ visible: true, x: clickX, y: clickY });
    }

    render(){
        return (
           
            <div class="rand">
                <p onContextMenu = {this.handleContext}>This is a context menu test </p>
                {this.state.visible? this.returnMenu() : null}
            </div>
        )
    }
}

export default Testing2;