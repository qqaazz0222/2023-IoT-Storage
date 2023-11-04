import axios from "axios";
import "./Styles/StorageInfo.css";
import { useEffect, useState } from "react";

const URL = process.env.REACT_APP_URL;

const StorageInfo = () => {
    const get_storage_info = async () => {
        const response = await axios.get(URL + "/system/disk");
        setStorage(response.data);
    };
    const [storage, setStorage] = useState([]);
    useEffect(() => {
        get_storage_info();
    }, []);
    return (
        <div id="storageInfo">
            <div className="titleWrap">저장소 요약</div>
            <div className="contentWrap">
                <span>총 {storage.length}개 저장소</span>
                <div className="listWrap">
                    {storage.map((item, idx) => (
                        <div className="item">
                            <div className="itemName">{item.device}</div>
                            <div className="itemInfo">
                                <div className="row">
                                    <div className="key">용량</div>
                                    <div className="value">{item.total}</div>
                                </div>
                                <div className="row">
                                    <div className="key">사용 가능</div>
                                    <div className="value">{item.free}</div>
                                </div>
                                <div className="row">
                                    <div className="key">사용됨</div>
                                    <div className="value">{item.used}</div>
                                </div>
                                <div className="barWrap">
                                    <div
                                        className="bar"
                                        style={{
                                            width: item.use + "%",
                                        }}
                                    />
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default StorageInfo;
