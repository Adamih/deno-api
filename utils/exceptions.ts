interface IRequestError {
  status: number;
}

class RequestError extends Error implements IRequestError {
  private _status: number;
  public get status(): number {
    return this._status;
  }
  public set status(v: number) {
    this._status = v;
  }
  constructor(status: number, ...args: any) {
    super(...args);
    this._status = status;
  }
}

export { RequestError };
