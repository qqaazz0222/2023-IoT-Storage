import axios from "axios";

import Header from "../Components/Header";
import "./Styles/Storage.css";
import { useEffect, useRef, useState } from "react";
import FileIcon from "../Components/FileIcon";
import Loading from "../Components/Loading";
import Upload from "../Components/Upload";

const URL = process.env.REACT_APP_URL;

const Storage = () => {
    const [isLoading, setIsLoading] = useState(true);
    const [storage, setStorage] = useState([
        { device: "", type: "", total: "", free: "", used: "" },
    ]);
    const [directory, setDirectory] = useState([]);
    const [selIdx, setSelIdx] = useState(0);
    const [path, setPath] = useState("");
    const [isUpload, setIsUpload] = useState(false);
    const [file, setFile] = useState();
    const get_storage_info = async () => {
        setIsLoading(true);
        const response = await axios.get(URL + "/system/disk");
        setStorage(response.data);
        setIsLoading(false);
    };
    const get_directory_info = async (path) => {
        setIsLoading(true);
        const response = await axios.post(URL + "/storage/read", {
            path: path,
        });
        setDirectory(response.data);
        setIsLoading(false);
    };
    const upload_file = async () => {
        setIsLoading(true);
        let formData = new FormData();
        formData.append("path", path);
        formData.append("file", file);
        const response = await axios.post(URL + "/storage/upload", formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        });
        get_directory_info(path);
        setIsUpload(false);
        setIsLoading(false);
    };
    const download_file = async (path, name) => {
        setIsLoading(true);
        const response = await axios.post(URL + "/storage/download", {
            path: path,
        });
        const url = window.URL.createObjectURL(
            new Blob([response.data], {
                type: `${response.headers["content-type"]}`,
            })
        );

        let link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", name);

        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);

        window.URL.revokeObjectURL(url); // memory 해제
        setIsLoading(false);
    };
    const chgPath = (name) => {
        setPath(path + "/" + name);
    };
    const downFile = (name) => {
        const p = path + "/" + name;
        download_file(p, name);
    };
    const goTop = () => {
        setPath(path.substr(0, path.lastIndexOf("/")));
    };
    useEffect(() => {
        get_storage_info();
    }, []);
    useEffect(() => {
        if (storage[0].device !== "" && storage[0].mount !== "") {
            setPath(storage[selIdx].mount);
        }
    }, [selIdx, storage]);
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
                    <div className="func">
                        <button
                            onClick={() => {
                                setIsUpload(!isUpload);
                            }}
                        >
                            파일 업로드
                        </button>
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
                            {storage[selIdx].mount === path ? (
                                <></>
                            ) : (
                                <FileIcon
                                    name={"상위 폴더"}
                                    ext={"back"}
                                    goTop={() => {
                                        console.log("[GO TOP FUCN]");
                                        goTop();
                                    }}
                                />
                            )}

                            {directory.map((item, idx) => (
                                <>
                                    {item.name[0] !== "." ? (
                                        <>
                                            <FileIcon
                                                name={item.name}
                                                ext={item.ext}
                                                chgPath={(name) => {
                                                    chgPath(name);
                                                }}
                                                downFile={(name) => {
                                                    downFile(name);
                                                }}
                                            />
                                        </>
                                    ) : (
                                        <></>
                                    )}
                                </>
                            ))}
                        </div>
                        {isUpload && (
                            <Upload
                                uploadFunc={upload_file}
                                setFile={setFile}
                                setIsUpload={setIsUpload}
                            />
                        )}
                        {isLoading && <Loading />}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Storage;
