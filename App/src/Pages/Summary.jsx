import Header from "../Components/Header";
import StorageInfo from "../Components/StorageInfo";
import SystemInfo from "../Components/SystemInfo";

import "./Styles/Summary.css";

const Summary = () => {
    return (
        <div id="summary">
            <Header />
            <div className="body">
                <div className="row">
                    <SystemInfo />
                </div>
                <div className="row">
                    <StorageInfo />
                </div>
            </div>
        </div>
    );
};

export default Summary;
