import React, { Component } from "react";
import SolrConnector from "node_modules/react-solr-connector";
import SolrConnectorDemo from "./SolrConnectorDemo";

class ApiData extends Component {
  constructor(props) {
    super(props);
    this.state = {
      searchParams: null
    };
  }

  doSearch(searchParams) {
    this.setState({ searchParams });
  }

  render() {
    return (
      <SolrConnector searchParams={this.state.searchParams}>
        <SolrConnectorDemo doSearch={this.doSearch.bind(this)} />
      </SolrConnector>
    );
  }
}

export default ApiData;
