proto.SearchService.SearchResponse.toObject = function(e, t) {
  var a = {
  status: r.Message.getFieldWithDefault(t, 1, !1),
      message: r.Message.getFieldWithDefault(t, 2, ""),
      count: r.Message.getFieldWithDefault(t, 3, 0),
      resourcesList: r.Message.toObjectList(t.getResourcesList(), o.Resource.toObject, e)
      };
      return e && (a.$jspbMessageInstance = t),
      a
}


proto.com.wanfangdata.resource.Resource.toObject = function(e, t) {
var a, s = {
    type: r.Message.getFieldWithDefault(t, 1, ""),
    originsList: r.Message.toObjectList(t.getOriginsList(), proto.com.wanfangdata.resource.Origin.toObject, e),
    uid: r.Message.getFieldWithDefault(t, 3, ""),
    claw: (a = t.getClaw()) && f.Claw.toObject(e, a),
    conference: (a = t.getConference()) && u.Conference.toObject(e, a),
    cstad: (a = t.getCstad()) && g.Cstad.toObject(e, a),
    magazine: (a = t.getMagazine()) && o.Magazine.toObject(e, a),
    meeting: (a = t.getMeeting()) && n.Meeting.toObject(e, a),
    nstr: (a = t.getNstr()) && h.Nstr.toObject(e, a),
    patent: (a = t.getPatent()) && d.Patent.toObject(e, a),
    periodical: (a = t.getPeriodical()) && c.Periodical.toObject(e, a),
    standard: (a = t.getStandard()) && p.Standard.toObject(e, a),
    thesis: (a = t.getThesis()) && l.Thesis.toObject(e, a),
    thesiscatalog: (a = t.getThesiscatalog()) && v.ThesisCatalog.toObject(e, a),
    video: (a = t.getVideo()) && m.Video.toObject(e, a),
    localchronicle: (a = t.getLocalchronicle()) && S.LocalChronicle.toObject(e, a),
    localchronicleitem: (a = t.getLocalchronicleitem()) && y.LocalChronicleItem.toObject(e, a),
    book: (a = t.getBook()) && w.Book.toObject(e, a)
    };
    return e && (s.$jspbMessageInstance = t),
    s
}

proto.com.wanfangdata.resource.Periodical.toObject = function(e, t) {
    var a, s = {
        id: r.Message.getFieldWithDefault(t, 1, ""),
        titleList: null == (a = r.Message.getRepeatedField(t, 2)) ? void 0 : a,
        creatorList: null == (a = r.Message.getRepeatedField(t, 3)) ? void 0 : a,
        firstcreator: r.Message.getFieldWithDefault(t, 4, ""),
        scholaridList: null == (a = r.Message.getRepeatedField(t, 5)) ? void 0 : a,
        foreigncreatorList: null == (a = r.Message.getRepeatedField(t, 6)) ? void 0 : a,
        creatorforsearchList: null == (a = r.Message.getRepeatedField(t, 7)) ? void 0 : a,
        organizationnormList: null == (a = r.Message.getRepeatedField(t, 8)) ? void 0 : a,
        organizationnewList: null == (a = r.Message.getRepeatedField(t, 9)) ? void 0 : a,
        originalorganizationList: null == (a = r.Message.getRepeatedField(t, 10)) ? void 0 : a,
        organizationforsearchList: null == (a = r.Message.getRepeatedField(t, 11)) ? void 0 : a,
        originalclasscodeList: null == (a = r.Message.getRepeatedField(t, 12)) ? void 0 : a,
        machinedclasscodeList: null == (a = r.Message.getRepeatedField(t, 13)) ? void 0 : a,
        classcodeforsearchList: null == (a = r.Message.getRepeatedField(t, 14)) ? void 0 : a,
        contentsearchList: null == (a = r.Message.getRepeatedField(t, 15)) ? void 0 : a,
        keywordsList: null == (a = r.Message.getRepeatedField(t, 16)) ? void 0 : a,
        foreignkeywordsList: null == (a = r.Message.getRepeatedField(t, 17)) ? void 0 : a,
        machinedkeywordsList: null == (a = r.Message.getRepeatedField(t, 18)) ? void 0 : a,
        keywordforsearchList: null == (a = r.Message.getRepeatedField(t, 19)) ? void 0 : a,
        abstractList: null == (a = r.Message.getRepeatedField(t, 20)) ? void 0 : a,
        citedcount: r.Message.getFieldWithDefault(t, 21, 0),
        periodicalid: r.Message.getFieldWithDefault(t, 22, ""),
        periodicaltitleforsearchList: null == (a = r.Message.getRepeatedField(t, 23)) ? void 0 : a,
        periodicaltitleList: null == (a = r.Message.getRepeatedField(t, 24)) ? void 0 : a,
        sourcedbList: null == (a = r.Message.getRepeatedField(t, 25)) ? void 0 : a,
        isoa: r.Message.getBooleanFieldWithDefault(t, 26, !1),
        fundList: null == (a = r.Message.getRepeatedField(t, 27)) ? void 0 : a,
        publishdate: r.Message.getFieldWithDefault(t, 28, ""),
        metadataonlinedate: r.Message.getFieldWithDefault(t, 29, ""),
        fulltextonlinedate: r.Message.getFieldWithDefault(t, 30, ""),
        servicemode: r.Message.getFieldWithDefault(t, 31, 0),
        hasfulltext: r.Message.getBooleanFieldWithDefault(t, 32, !1),
        publishyear: r.Message.getFieldWithDefault(t, 33, 0),
        issue: r.Message.getFieldWithDefault(t, 34, ""),
        volum: r.Message.getFieldWithDefault(t, 35, ""),
        page: r.Message.getFieldWithDefault(t, 36, ""),
        pageno: r.Message.getFieldWithDefault(t, 37, ""),
        columnList: null == (a = r.Message.getRepeatedField(t, 38)) ? void 0 : a,
        coreperiodicalList: null == (a = r.Message.getRepeatedField(t, 39)) ? void 0 : a,
        fulltextpath: r.Message.getFieldWithDefault(t, 40, ""),
        doi: r.Message.getFieldWithDefault(t, 41, ""),
        authororgList: null == (a = r.Message.getRepeatedField(t, 42)) ? void 0 : a,
        thirdpartyurlList: null == (a = r.Message.getRepeatedField(t, 43)) ? void 0 : a,
        language: r.Message.getFieldWithDefault(t, 44, ""),
        issn: r.Message.getFieldWithDefault(t, 45, ""),
        cn: r.Message.getFieldWithDefault(t, 46, ""),
        sequenceinissue: r.Message.getFieldWithDefault(t, 47, 0),
        metadataviewcount: r.Message.getFieldWithDefault(t, 48, 0),
        thirdpartylinkclickcount: r.Message.getFieldWithDefault(t, 49, 0),
        downloadcount: r.Message.getFieldWithDefault(t, 50, 0),
        prepublishversion: r.Message.getFieldWithDefault(t, 51, ""),
        prepublishgroupid: r.Message.getFieldWithDefault(t, 52, ""),
        publishstatus: r.Message.getFieldWithDefault(t, 53, ""),
        type: r.Message.getFieldWithDefault(t, 54, ""),
        singlesourcedb: r.Message.getFieldWithDefault(t, 55, ""),
        exportcount: r.Message.getFieldWithDefault(t, 56, 0),
        periodicalclasscodeList: null == (a = r.Message.getRepeatedField(t, 57)) ? void 0 : a,
        scholaridauthorList: null == (a = r.Message.getRepeatedField(t, 58)) ? void 0 : a,
        citedscore: r.Message.getFloatingPointFieldWithDefault(t, 59, 0),
        downloadscore: r.Message.getFloatingPointFieldWithDefault(t, 60, 0),
        yearscore: r.Message.getFloatingPointFieldWithDefault(t, 61, 0),
        typescore: r.Message.getFieldWithDefault(t, 62, 0),
        projectidList: null == (a = r.Message.getRepeatedField(t, 63)) ? void 0 : a,
        fundgroupnameList: null == (a = r.Message.getRepeatedField(t, 64)) ? void 0 : a,
        projectgrantnoList: null == (a = r.Message.getRepeatedField(t, 65)) ? void 0 : a,
        isthirdservice: r.Message.getBooleanFieldWithDefault(t, 66, !1),
        lastmodifiedtime: r.Message.getFieldWithDefault(t, 67, "")
    };
    return e && (s.$jspbMessageInstance = t),
        s
}

proto.com.wanfangdata.resource.Origin.toObject = function(e, t) {
var a = {
type: r.Message.getFieldWithDefault(t, 1, 0),
    status: r.Message.getFieldWithDefault(t, 2, !1),
    thirdpartyList: r.Message.toObjectList(t.getThirdpartyList(), proto.com.wanfangdata.resource.ThirdParty.toObject, e)
    };
    return e && (a.$jspbMessageInstance = t),
    a
}


proto.SearchService.SearchResponse.serializeBinaryToWriter = function(e, t) {
var a = void 0;
    a = e.getStatus(),
    a && t.writeBool(1, a),
    a = e.getMessage(),
    a.length > 0 && t.writeString(2, a),
a = e.getCount(),
    0 !== a && t.writeInt64(3, a),
    a = e.getResourcesList(),
    a.length > 0 && t.writeRepeatedMessage(4, a, o.Resource.serializeBinaryToWriter)
}