import "./CustomContext.css";
import React, { Component } from "react";
import Testing from "./Testing";

class CustomContext extends Component{
    constructor(props) {
        super(props);
        this.state={
            visible: false,
            x: 0,
            y: 0,
            components:[]
            };

        this.contextRef = React.createRef();
    }

    click(index){

        if(this.props.items[index].callback){
            this.props.items[index].callback();
            var self = this;
            const newComponents = [...this.state.components];
            this.setState({
                components:newComponents
            });
        }
        else{
            console.log("Callback isn't registered");
        }
    }
    
    
    componentDidMount(){

        var self=this;
        document.addEventListener('contextmenu', function(event){
        event.preventDefault();
        const clickX = event.clientX;
        const clickY = event.clientY;
        self.setState({ visible: true, x: clickX, y: clickY });
    
    });
    
    document.addEventListener('click', function(event){
        if( self.contextRef.current.id == 'customcontext'){
            self.click(event.target.getAttribute('index'));
        }
        event.preventDefault();
        self.setState({visible:false, x:0, y:0});
        });
    }

    
    returnMenu(items){
        var myStyle = {
        position: 'absolute',
        top: `${this.state.y}px`,
        left:`${this.state.x+5}px`
        }
    
        return <div className='custom-context' id='customcontext' style={myStyle} ref={this.contextRef}>
            {items.map((item, index, arr) =>{
            
            if(arr.length-1==index){
                
                return <div key={index} className='custom-context-item-last' index={index}>{item.label}</div>
            }
            else{
                return <div key={index} className='custom-context-item' index={index}>{item.label}</div>
            }
            })}
            </div>;
    }

    render(){
        return (
            <div id="cmenu">
                
                {this.state.visible? this.returnMenu(this.props.items): null}
                
            </div>
        )
    }
}

export default CustomContext;