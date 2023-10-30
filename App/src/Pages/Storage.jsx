import axios from "axios";

import Header from "../Components/Header";
import "./Styles/Storage.css";
import { useEffect, useState } from "react";
import IconFolder from "../Images/IconFolder.png";

const URL = "http://192.168.0.84:3001";

const Storage = () => {
    const get_storage_info = async () => {
        const response = await axios.get(URL + "/system/disk");
        console.log(response.data);
        setStorage(response.data);
    };
    const get_directory_info = async (path) => {
        const response = await axios.post(URL + "/storage/read", {
            path: path,
        });
        console.log(response.data);
        setDirectory(response.data);
    };
    const [storage, setStorage] = useState([
        { device: "", type: "", total: "", free: "", used: "" },
    ]);
    const [directory, setDirectory] = useState([]);
    const [selIdx, setSelIdx] = useState(0);
    const [path, setPath] = useState("");
    useEffect(() => {
        get_storage_info();
    }, []);
    useEffect(() => {
        if (storage[0].device !== "") {
            setPath(storage[selIdx].mount);
        }
    }, [selIdx]);
    useEffect(() => {
        if (path !== "") {
            console.log(path);
            get_directory_info(path);
        }
    }, [path]);
    return (
        <div id="storage">
            <Header />
            <div className="body">
                <div className="optionWrap">
                    <div className="title">저장소</div>
                    <select
                        name="storage"
                        onChange={(e) => {
                            setSelIdx(e.target.value);
                        }}
                    >
                        {storage.map((item, idx) => (
                            <option value={idx}>{`#${idx + 1} ${
                                item.device
                            }`}</option>
                        ))}
                    </select>
                </div>
                <div className="contentWrap">
                    <div className="infoWrap">
                        <div className="row">
                            <div className="key">저장소 이름</div>
                        </div>
                        <div className="row">
                            <div className="value">
                                {storage[selIdx].device}
                            </div>
                        </div>
                        <div className="row">
                            <div className="key">포맷</div>
                            <div className="value">{storage[selIdx].type}</div>
                        </div>
                        <div className="row">
                            <div className="key">용량</div>
                            <div className="value">{storage[selIdx].total}</div>
                        </div>
                        <div className="row">
                            <div className="key">사용 가능</div>
                            <div className="value">{storage[selIdx].free}</div>
                        </div>
                        <div className="row">
                            <div className="key">사용됨</div>
                            <div className="value">{storage[selIdx].used}</div>
                        </div>
                    </div>
                    <div className="folderWrap">
                        <div className="directoryWrap">
                            {directory.map((item, idx) => (
                                <>
                                    {item.name[0] !== "." ? (
                                        <div
                                            className="item"
                                            title={item.name}
                                            onClick={() => {
                                                setPath(path + "/" + item.name);
                                            }}
                                        >
                                            <img
                                                src={IconFolder}
                                                alt={item.name}
                                                srcset=""
                                            />
                                            <span>{item.name}</span>
                                        </div>
                                    ) : (
                                        <></>
                                    )}
                                </>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Storage;
