#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: error.py


class NewsPushError(Exception):
    ...

# Token相关异常


class TokenError(NewsPushError):
    ...


class TokenNotFoundError(TokenError):
    ...

# WeatherApi相关异常


class WeatherError(NewsPushError):
    ...


class GetWeatherFaildError(WeatherError):
    ...

# CityDate 相关错误


class CityDataError(NewsPushError):
    ...


class CsvParserError(CityDataError):
    ...

# 邮件相关


class EmailServiceError(NewsPushError):
    ...


class EmailFormatError(EmailServiceError):
    ...


class EmailServerLoginError(EmailServiceError):
    ...


class EmailSendError(EmailServiceError):
    ...
