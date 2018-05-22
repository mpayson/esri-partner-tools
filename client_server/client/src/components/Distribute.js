import React, { Component } from 'react';
import './Register.css';

// CONSTANTS THAT DEFINE SET UP BEHAVIOR
const GROUPSCHEMA = {
  "title": "My Test Title",
  "tags": "test, group, poc, scripts",
  "description": "Test group for partner python scripts",
  "access": 'private',
  "is_invitation_only": true,
  "users_update_items": false
};

const ITEMID = "90dffd24537240a59eede871ade5856a";
const APPID = "1bbda506fdfd4c82a90fea57426f5603";

// UTIL FUNCTIONS
const getPortalUrl = (urlKey) => urlKey ? `https://${urlKey}.maps.arcgis.com` : "https://arcgis.com";

const getStatusItem = (status, text) => {
  const doneClass = "icon-ui-checkbox-checked icon-ui-green";
  const pendClass = "icon-ui-checkbox-unchecked icon-ui-gray text-dark-gray";
  const activeClass = "text-dark-gray";
  const indicator = <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" className="svg-icon indicator"><path d="M27.518 8.338c.324.37.772.94 1.261 1.727a13.499 13.499 0 0 1 1.986 7.41c-.019 3.243-1.41 7.185-4.559 10.081-3.085 2.902-7.94 4.492-12.611 3.566-4.697-.832-8.864-4.161-10.853-8.38-2.043-4.23-1.863-9.035-.373-12.647 1.463-3.672 4.051-6.09 6.098-7.421C10.551 1.336 12.092.889 12.389.802c1.234-.356 2.457-.18 3.282.309.839.511 1.281 1.259 1.276 2.105-.079 1.717-1.406 3.039-2.86 3.478-.19.051-1.158.258-2.564.99a10.6 10.6 0 0 0-4.43 4.522c-1.216 2.318-1.698 5.672-.504 8.872 1.158 3.185 4.042 6.059 7.693 7.058 3.629 1.078 7.773.199 10.671-2.06 2.944-2.244 4.563-5.648 4.855-8.66.369-3.046-.465-5.615-1.261-7.222a13.163 13.163 0 0 0-1.084-1.812l-.45-.601.504.559z"/></svg>;

  switch(status) {
    case "active":
      return <h3 key={text} className={activeClass}>{indicator}{text}</h3>;
    case "done":
      return <h3 key={text} className={doneClass}>{text}</h3>;
    default:
      return <h3 key={text} className={pendClass}>{text}</h3>;
  }
}

// Displayed text
const actionText = {
  "create": "Create & share a group",
  "share": "Publish & share an item",
  "clone": "Clone an application"
}

// The main component
class Distribute extends Component {

  urlKey = null
  state = {
    "create": "pending",
    "share": "pending",
    "clone": "pending",
    "result": null,
    "working": false
  }

  constructor(props, context){
    super(props, context);
    this.onGoClick = this.onGoClick.bind(this);
  }

  onGoClick(evt){
    console.log(this.props.session.portal);
    this.createGroup();
  }

  // Create a group then move on
  createGroup(){
    this.setState({
      "create": "active",
      "working": true
    });
    const data = {
      token: this.props.session.token,
      username: this.props.session.username,
      schema: GROUPSCHEMA
    };
    fetch('/distribute/group', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: new Headers({
        'Content-Type': 'application/json'
      })
    }).then(res => res.json())
    .then(rjson => {
      this.urlKey = rjson.urlKey;
      this.setState({"create": "done"});
      this.copyItem(rjson.groupId);
    });

  }

  // Copy a new item (copies an existing item like a template) then shares
  // This item stays in your control rather than copied to an end-user's deployment
  copyItem(groupId){
    this.setState({"share": "active"});
    const data = {
      token: this.props.session.token,
      username: this.props.session.username,
      copyIds: [ITEMID]
    };
    fetch(`/distribute/group/${groupId}`, {
      method: 'PUT',
      body: JSON.stringify(data),
      headers: new Headers({
        'Content-Type': 'application/json'
      })
    }).then(res => res.json())
    .then(rjson => {
      this.setState({"share": "done"});
      this.cloneItem(groupId, rjson.copyIds);
    });
  }

  // Clone an item (clones an existing item like a template then shares)
  // This item is copied to an end users deployment
  // In this case, I'm cloning an application pre-configured to work with the ITEMID
  // Rather than clone the ITEM as well, I'm passing an itemMap so it references the previously copied item
  cloneItem(groupId, itemMap){
    this.setState({"clone": "active"});
    const data = {
      token: this.props.session.token,
      username: this.props.session.username,
      cloneIds: [APPID],
      itemMap: itemMap
    };
    fetch(`/distribute/group/${groupId}`, {
      method: 'PUT',
      body: JSON.stringify(data),
      headers: new Headers({
        'Content-Type': 'application/json'
      })
    }).then(res => res.json())
    .then(rjson => this.setState({
      "clone": "done",
      "result": groupId
    }));
  }

  // Show some cool stuff!
  render(){
    const btnClass = this.state.working ? "btn btn-disabled" : "btn";
    const footer = this.state.result
      ? <h3><a target="_blank" href={`${getPortalUrl(this.urlKey)}/home/group.html?id=${this.state.result}`}>Check it out!</a></h3>
      : <button className={btnClass} onClick={this.onGoClick}>Go!</button>;

    return (
      <div className="msg-background">
        <div className="msg-window">
          <div className="card block">
            <div className="card-content">
              <h1>Let's get you started!</h1>
              <ul className="list-plain">
                {getStatusItem(this.state["create"], actionText["create"])}
                {getStatusItem(this.state["share"], actionText["share"])}
                {getStatusItem(this.state["clone"], actionText["clone"])}
              </ul>
              {footer}
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default Distribute;