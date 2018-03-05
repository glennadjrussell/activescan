from flask_injector import inject
import logging
import nmap
import collections

log = logging.getLogger(__name__)

class IPScanner(object):
    """
    Scans IP addresses, duh
    """
    def __init__(self):
        self.nm = nmap.PortScanner()

    def get_scan(self, ipAddress: str) -> dict:
        return {}

    def health(self) -> dict:
        return {"status": "ok"}

    def run_scan(self, ipAddress: str) -> dict:
        log.info("Scanning %s", ipAddress)
        self.nm.scan(ipAddress, '22-443')
        log.info("Scan complete")


        result = {}
        for host in self.nm.all_hosts():
            host_result = []
            for proto in self.nm[host].all_protocols():
                ports = self.nm[host][proto].keys()
                #ports.sort()
                for port in ports:
                    result_body = self.nm[host][proto][port]
                    result_body['port'] = str(port)
                    host_result.append(result_body)

            result[host] = host_result

        log.info(result)

        return result

class_instance = IPScanner()
