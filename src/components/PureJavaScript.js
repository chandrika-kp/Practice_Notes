import React from "react";
function PureJavaScript () {
//     let count = 5;
  
    return (
      
      React.createElement('form', {},
      React.createElement("h1", {}, "Login"),
      React.createElement('input', {type: 'text',placeholder:'Name', value: ''}),
      React.createElement('br', {}),React.createElement('br', {}), 
      React.createElement('input', {type: 'password', placeholder: 'password',
                           value: '',}), 
      React.createElement('br', {}), React.createElement('br', {}), 
      React.createElement('button', {type: 'submit'}, "Login"))
      
    /* {instead of using separate html,css,javascript files, 
       in react we are using html elements in the react components as js files }*/

    /*  Instead of using purejavaScript we are using JavaScript Syntax Extension (JSX)
       -----> As the browser doesnot understand JSX,BABEL plugins convert this JSX to pure JavaScript
       -----> Js experssion { } in JSX
       -----> you may render multiple react elements like <h1> , <p> etc throws error to 
              overcome that all elements should be wrapped b/w 
              <React.Fragment> </React.Fragment> or 
              <> </> or
              <div> </div> */


    //   <div>
    //   <h1> { "Expression to be evaluated "} </h1>
    //   <h1>{count}</h1>
    //   <h2>{count * count}</h2>

    // </div>
    
  
    )
  }
  export default PureJavaScript
  
